all: checkVirtual prep start

checkVirtual:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate a virtualenv to continue (cf https://virtualenv.readthedocs.org)" >&2 ;\
		exit 1; \
	fi

prep:
	pip install -r requirements.txt

start:
	python market.py

test tests:
	@echo "Make sure the Market is running, then Y to continue or N to quit:"
	@read junk ;\
	case $$junk in \
	  y|Y)  nosetests ;\
            ;; \
      *)    ;; \
    esac
