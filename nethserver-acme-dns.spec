Summary: NethServer configuration for acme-dns
%define name nethserver-acme-dns
%define version 0.0.1
%define release 6
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: nethserver-devtools
Requires: acme-dns
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