all: checkVirtual prep ratingsService

checkVirtual:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate a virtualenv to continue (cf https://virtualenv.readthedocs.org)" >&2 ;\
		exit 1; \
	fi

prep:
	pip install datawire-quark

ratingsService:
	quark install --python ../ratings/ratings.q
