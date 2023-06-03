install:
	@python3 setup.py install
	@cp rhusbd rhusb /bin/
	@cp rhusbd@.service /usr/lib/systemd/system/
	@cp completion/rhusb /etc/bash_completion.d/
	@install -d /etc/rhusbd
	@echo ""
	@echo "Installed server, client, and service files."
	@echo "Now copy the relevant json config files to /etc/rhusbd/"
	@echo "and udev rules to /usr/lib/udev/rules.d/"
