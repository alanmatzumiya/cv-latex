#!/usr/bin/env bash


pdflatex "cv.tex";

for i in aux log out tex
do
  if [ -f "cv.$i" ]
    then
      rm "cv.$i"
  fi
done