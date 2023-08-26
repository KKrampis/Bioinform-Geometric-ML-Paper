#makes html
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex GeoDeepLearnBio_v2.adoc
#makes docbook xml (as intermediate for pdf conversion)
asciidoctor -v -r asciidoctor-diagram -r asciidoctor-bibtex -b docbook GeoDeepLearnBio_v2.adoc
#pandoc used to convert docbook to pdf
pandoc -V geometry:margin=1.15in -f docbook GeoDeepLearnBio_v2.xml -o GeoDeepLearnBio_v2.pdf
#pandoc used to convert docbook to doc
pandoc -f docbook GeoDeepLearnBio_v2.xml -o GeoDeepLearnBio_v2.docx
