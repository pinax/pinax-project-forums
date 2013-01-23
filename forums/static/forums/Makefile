BOOTSTRAP_LESS = ./less/forums.less
CSS_OUTPUT_FILENAME = forums.css
LESS_COMPRESSOR ?= `which lessc`

#
# BUILD SITE MEDIA
# lessc is required
#

build:
	mkdir -p css
	lessc --yui-compress ${BOOTSTRAP_LESS} > css/${CSS_OUTPUT_FILENAME}

