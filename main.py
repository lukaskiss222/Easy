import argparse
from builder import builder





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File to compile")
    parser.add_argument("-O", "--optimize", help="Run optimization on program",
                        action="store_true")
    parser.add_argument("-o", "--output",
                        help="Name for output file",
                        type=str,
                        default=None)
    parser.add_argument("--x86",
                        help="Compile to X86 architecture, 4Byte pointer size",
                        action="store_true")
    args = parser.parse_args()

    file_in = args.filename
    if args.output is None:
        file_out = file_in.split(".")[0] + ".ll"
    else:
        file_out = args.output

    b = builder()

    with open(file_in, "r") as f:
        program = f.read()
    compiled = b.traslate(program, optimize=args.optimize,
                          mode32=args.x86)

    with open(file_out,"w") as f:
        f.write(compiled)



if __name__ == "__main__":
    main()