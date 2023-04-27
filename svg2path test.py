##svg2path test 
import svgpathtools

paths, attributes = svgpathtools.svg2paths('/home/gchen328/GIT_REPOS/ericwork/edalvaArtProj/adversarial_example_BnW_BnW.svg')

svgpathtools.wsvg(paths, attributes=attributes, filename='svg2paths_output.svg')