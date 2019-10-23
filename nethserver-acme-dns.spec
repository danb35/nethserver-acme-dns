Summary: NethServer configuration for acme-dns
%define name nethserver-acme-dns
%define version 0.2.0
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://github.com/danb35/nethserver-acme-dns

BuildRequires: nethserver-devtools
Requires: acme-dns >= 0.8
Requires: nethserver-release = 7
#AutoReq: no

%description
NethServer configuration for acme-dns
(https://github.com/joohoi/acme-dns)

%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} $RPM_BUILD_ROOT > default.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files -f default.lst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Oct 23 2019 Dan Brown <dan@familybrown.org> 0.2.0-1.ns7
- Update to acme-dns >= 0.8
- By default, acme-dns obtains its own cert

* Thu Mar 28 2019 Dan Brown <dan@familybrown.org> 0.1.0-4.ns7
- Fix logic for DisableRegistration

* Wed Mar 27 2019 Dan Brown <dan@familybrown.org> 0.1.0-3.ns7
- Add README
- Add config option to disable API registration

* Thu Mar 21 2019 Dan Brown <dan@familybrown.org> - 0.1.0-2.ns7
- Change ownership of /etc/acme-dns/config.cfg to acme-dns user

* Wed Mar  6 2019 Dan Brown <dan@familybrown.org> - 0.1.0-1.ns7
- Update for acme-dns 0.7, allow TCP and UDP connections

* Thu Sep  6 2018 Dan Brown <dan@familybrown.org> - 0.0.1-7
- Added ability to configure domain

* Mon Jun 18 2018 Dan Brown <dan@familybrown.org> - 0.0.1-6.el7
- Changed default access for API to green
* Sun Jun 17 2018 Dan Brown <dan@familybrown.org> - 0.0.1-5.el7
- Fixed one missing correction to acme-dns
* Sun Jun 17 2018 Dan Brown <dan@familybrown.org> - 0.0.1-4.el7
- Correct config database keys to acme-dns and acme-dns-api
* Sun Jun 17 2018 Dan Brown <dan@familybrown.org> - 0.0.1-3.el7
- Fix 30api template
* Fri Jun 15 2018 Dan Brown <dan@familybrown.org> - 0.0.1-2.el7
- Added config option for ExternalIP
* Thu Jun 14 2018 Dan Brown <dan@familybrown.org> - 0.0.1-1.el7
- Initial release
