Name:      rockit-rhusb
Version:   %{_version}
Release:   1
Summary:   Temperature and humidity probe
Url:       https://github.com/rockit-astro/rhusbd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/rhusbd
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/rhusb %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/rhusbd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/rhusbd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/rhusb %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/rhusbd
%{__install} %{_sourcedir}/10-warwick-rhusb.rules %{buildroot}%{_udevrulesdir}

%package server
Summary:  Environment sensor server
Group:    Unspecified
Requires: python3-rockit-rhusb
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/rhusbd
%defattr(0644,root,root,-)
%{_unitdir}/rhusbd@.service

%package client
Summary:  Environment sensor client
Group:    Unspecified
Requires: python3-rockit-rhusb
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/rhusb
/etc/bash_completion.d/rhusb

%package data-warwick
Summary: Environment sensor data for Windmill Hill observatory
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-warwick-rhusb.rules
%{_sysconfdir}/rhusbd/warwick.json

%changelog
