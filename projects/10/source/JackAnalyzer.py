from source.JackTokenizer import JackTokenizer
from source.CompilationEngine  import CompilationEngine
import sys
import os
import glob

class JackAnalyzer():
    @classmethod
    def run(cls, input_file, output_file):
        tokenizer = JackTokenizer(input_file)
        compiler = CompilationEngine(tokenizer, output_file)
        compiler.compile_class()

    @classmethod
    def xml_output_file_for(cls, input_file):
        file_name = os.path.basename(input_file).split(".")[0]
        ext_name = ".xml"
        dir_name = os.path.dirname(input_file)
        return dir_name + "/" + file_name + ext_name


if __name__ == "__main__" and len(sys.argv) == 2:
    arg = sys.argv[1]

    # determine output file names
    if os.path.isfile(arg):
        files = [arg]
    elif os.path.isdir(arg):
        jack_path = os.path.join(arg, "*.jack")
        files = glob.glob(jack_path)

    for input_file in files:
        output_file_name = JackAnalyzer.xml_output_file_for(input_file)
        output_file = open(output_file_name, 'w')
        JackAnalyzer.run(input_file, output_file)
