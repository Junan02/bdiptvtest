lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")

# Flag to keep track if the next line is supposed to be a link
nextLineLink=False 

for line in open(infilename, "r"):

    # Check if the current line is a name line 
    if line.startswith("#EXTINF"):
        info=line
        nextLineLink=True
        continue

    # If we encounter an empty line, set back flag
    # Otherwise we would write the last info too 
    if line.strip()=="":
        nextLineLink=False
        continue

    # Check if this line is supposed to be a link
    if nextLineLink:

        # Check if we already seen the line
        if line not in lines_seen: # not a duplicate

            # Write both lines and add
            outfile.write(info)
            outfile.write(line)
            lines_seen.add(line)

            # Set back flag
            nextLineLink=False


outfile.close()
