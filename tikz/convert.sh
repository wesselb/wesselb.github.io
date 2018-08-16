#!/usr/bin/zsh

set -e

for file in ./*.pdf; do
    file=$(basename $file)
    file_png=$(echo $file | sed 's/pdf$/png/g')
    echo "Converting $file to $file_png..."
    convert -quality 90 -density 600x600 -trim \
        $file \
        ../assets/images/posts/$file_png
done


