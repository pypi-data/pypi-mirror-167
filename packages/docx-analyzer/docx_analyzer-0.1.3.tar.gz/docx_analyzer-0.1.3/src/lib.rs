use itertools::Itertools;
use pyo3::prelude::*;
use regex::Regex;
use std::collections::VecDeque;
use std::fs;
use std::io;
use std::io::Read;
use std::ops::Not;
use std::path::Path;
use std::path::PathBuf;
use walkdir::WalkDir;
use std::collections::HashMap;    

#[pyfunction]
fn analyze(path: String) -> PyResult<Vec<String>> {    
    let mut tag_translation = HashMap::new();
    
    unpack_zip(path);

    let mut tags = Vec::new();
    for file in WalkDir::new("analyzer_temp/") {
        let path = file.unwrap().path().to_owned();
        if path.is_file() {
            tags = [tags, analyze_doc(&path, &mut tag_translation)].concat();
        };
    }    
    
    for i in 0..tags.len() {
        let splitted: Vec<String> = tags[i].split(".").map(str::to_string).collect();
        match tag_translation.get(&splitted[0]) {
            Some(tag) => replace_tag(&mut tags, i, format!("{}.{}", tag, splitted[1])),
            None => println!("nothingness")
        }
    }

    let mut unique_tags: VecDeque<&String> = tags.iter().unique().collect();        

    let validated_tags = validate_tags_and_make_fields(unique_tags).unwrap();

    // clean temp folder
    fs::remove_dir_all("analyzer_temp/").unwrap();

    Ok(validated_tags)
}


#[pymodule]
fn docx_analyzer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(analyze, m)?)?;
    Ok(())
}

fn validate_tags_and_make_fields(tags: VecDeque<&String>) -> PyResult<Vec<String>> {
    // let mut fields = Vec::new();
    let mut fields = Vec::new();                
    

    for i in 0..tags.len() {    

    let splitted: VecDeque<&str> = tags[i].split(".").collect();        

        if splitted.len() == 2 {
            if splitted[0].is_empty().not() & splitted[1].is_empty().not() {
                let chars: Vec<char> = splitted[0].chars().collect();

                if chars.len() >= 3 {
                    fields.push(tags[i].to_owned());
                }
            }
        }
    }
    Ok(fields)
}

fn replace_tag(tags: &mut Vec<String>, index: usize, replacement: String) {
    tags.swap_remove(index);
    tags.push(replacement);
}

fn unpack_zip(path: String) {
    let fname = std::path::Path::new(&path);
    let file = fs::File::open(&fname).unwrap();

    let mut archive = zip::ZipArchive::new(file).unwrap();

    for i in 0..archive.len() {
        let mut file = archive.by_index(i).unwrap();
        let outpath = match file.enclosed_name() {
            Some(path) => path.to_owned(),
            None => continue,
        };

        if (*file.name()).ends_with('/') {
            fs::create_dir_all(&outpath).unwrap();
        } else {
            let outpath_new = PathBuf::from(
                "analyzer_temp/".to_owned() + outpath.file_name().unwrap().to_str().unwrap(),
            );
            if let Some(p) = outpath_new.parent() {
                if !p.exists() {
                    fs::create_dir_all(&p).unwrap();
                }
            }
            let mut outfile = fs::File::create(&outpath_new).unwrap();
            io::copy(&mut file, &mut outfile).unwrap();
        }
    }
}

fn analyze_doc(path: &Path, tag_translation: &mut HashMap<String, String>) -> Vec<String> {
    let file = fs::File::open(&path).unwrap();

    let mut archive = zip::ZipArchive::new(file).unwrap();

    let mut doc_in_zip = archive.by_name("word/document.xml").unwrap();

    let mut buffer = String::from("");
    doc_in_zip.read_to_string(&mut buffer).unwrap();

    let s_slice: &str = &buffer[..];
    let doc = roxmltree::Document::parse(&s_slice).unwrap();

    let mut doc_xml_nodes = doc.descendants();

    let mut doc_text = String::new();

    loop {
        match doc_xml_nodes.next() {
            Some(x) => {
                if x.has_tag_name("t") {
                    doc_text.push_str(x.text().unwrap());
                }
            }
            None => break,
        }
    }

    let regex = Regex::new(r"(?:(^|[^\{])\{\{)([^\}]*?)(?:\}\}(?:($|[^\}])))").unwrap();

    let mut mat = regex.find_iter(&doc_text);

    let mut regex_res = String::new();

    loop {
        match mat.next() {
            Some(x) => {
                regex_res.push_str(x.as_str());
            }
            None => break,
        }
    }

    regex_res = regex_res
        .replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace(")", "")
        .replace("(", "")
        .replace("/", "");

    let tags = regex_res.split_whitespace().map(str::to_string).collect();

    let tags_with_loops = loop_tags(&doc_text, tags, tag_translation);

    tags_with_loops
}

fn loop_tags(doc_text: &String, tags: Vec<String>, tag_translation: &mut HashMap<String, String>) -> Vec<String> {
    let regex = Regex::new(r"%(.*?)%").unwrap();

    let mut mat = regex.find_iter(&doc_text);

    let mut regex_res = String::new();

    loop {
        match mat.next() {
            Some(x) => {
                regex_res.push_str(x.as_str());
            }
            None => break,
        }
    }

    let loop_tag_list: Vec<String> = regex_res.split("%").map(str::to_string).collect();

    let mut validated_loop_tag_list = Vec::new();
    for i in 0..loop_tag_list.len() {
        let splitted: Vec<String> = loop_tag_list[i]
            .split_whitespace()
            .map(str::to_string)
            .collect();
        if splitted.is_empty().not() {
            if splitted[0] == "for" {
                for x in 0..tags.len() {
                    let splitted_tags: Vec<String> =
                        tags[x].split(".").map(str::to_string).collect();
                    if splitted_tags.is_empty().not() {
                        if splitted[1] == splitted_tags[0] {
                            tag_translation.insert(splitted[1].clone(), splitted[3].clone());
                            let new_tag = format!("{}.{}", splitted[3], splitted_tags[1]);
                            validated_loop_tag_list.push(new_tag);
                        } else {
                            validated_loop_tag_list.push(tags[x].clone());
                        }
                    }
                }
            } else if splitted[0] == "if" || splitted[0] == "elif" {
                let new_tag = format!("{}", splitted[1]);
                let splitted_tag: Vec<String> = splitted[1].split(".").map(str::to_string).collect();
                println!("{}", format!("{} -> {:?}", &splitted_tag[0], tag_translation.get(&splitted_tag[0]).to_owned()));
                validated_loop_tag_list.push(new_tag.clone());
            }
        }
    }

    validated_loop_tag_list
}
