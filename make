#!/usr/bin/env bash


name=$1

cd ./templates
pdflatex "$name.tex";

for i in aux log out
do
  if [ -f "$name.$i" ]
    then
      rm "$name.$i"
  fi
done

mv "$name.pdf" ../cv.pdf
