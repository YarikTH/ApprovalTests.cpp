import pypandoc
from pypandoc.pandoc_download import download_pandoc


def convertMarkdownDocsToRst():
    # TODO Only download pandoc if it's not found
    download_pandoc()

    # TODO make various edits to improve conversion, like removing the Table of Contents
    input_dir = '../../doc'
    output_dir = 'generated_docs'
    file_base_name = 'UsingCatch'
    convert_markdown_to_restructured_text(file_base_name, input_dir, output_dir)


def convert_markdown_to_restructured_text(file_base_name, input_dir, output_dir):
    output = pypandoc.convert_file(f'{input_dir}/{file_base_name}.md', 'rst',
                                   outputfile=f'{output_dir}/{file_base_name}.rst')
    assert output == ""
