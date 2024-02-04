import argparse
from extract_frame import extract_frame
from delete_duplicated_frames import delete_duplicated_frames
from extract_text import write_doc



def get_args():
    parser = argparse.ArgumentParser(prog="Weepie")
    subparsers = parser.add_subparsers(help="sub-command help", dest="cmd_name")

    parser_extractFrames = subparsers.add_parser('extractFrames', help='Extract frames from video')
    parser_extractFrames.add_argument("videoPath", help="Path to the video file")
    parser.add_argument("-i", "--imageDirPath", help="Path to the output directory of extracted frames", default="../data/img/")
    parser_extractFrames.add_argument("-freq", "--frequency", help="Frequency of extracting frames", default=10)

    parser_delDupFrames = subparsers.add_parser("delDupFrames", help="Delete duplicated frames")
    parser_delDupFrames.add_argument("-t", "--threshold", help="Threshold of MSE of determining similarity of two images", default=2)

    parser_extractText = subparsers.add_parser("extractText", help="Extract text from images and write to disk")
    parser_extractText.add_argument("-o", "--outputPath", help="Path and filename to the output text file", default="../out/weepyweepie.txt")

    args = parser.parse_args()
    return args



def main():
    args = get_args()

    # $ python3 weepie.py -i ../data/img/cad/ extractFrames ../data/video/cad.mp4  
    if args.cmd_name == "extractFrames":
        extract_frame(args.videoPath, args.imageDirPath, args.frequency)

    # $ python3 weepie.py -i ../data/img/cad/ delDupFrames 
    if args.cmd_name == "delDupFrames":
        delete_duplicated_frames(args.imageDirPath, args.threshold)
    
    # $ python3 weepie.py -i ../data/img/cad/ extractText -o ../out/cad.txt
    if args.cmd_name == "extractText":
        write_doc(args.imageDirPath, args.outputPath)


if __name__ == "__main__":
    main()