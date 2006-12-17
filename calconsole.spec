#
Summary:	Calconsole is a calendar and schedule in mode command line
Summary(pl):	Calconsole jest kalendarzem i harmonogramem zadañ z linii poleceñ
Name:		calconsole
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://calconsole.losinvisibles.net/%{name}-%{version}.tar.gz
# Source0-md5:	abc17425cbeae6def877928ed1c50ad9
Patch0:		%{name}-DESTDIR.patch
URL:		http://calconsole.losinvisibles.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calconsole is a calendar and schedule in mode command line. Like a cal
with schedule. Calconsole works with files ics.

%description -l pl
Calconsole jest kalendarzem i harmonogramem zadañ z linii poleceñ.
Podobnie jak komenda cal, ale z harmonogramem zadañ. Calconsole
pracuje z plikami ics.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/zoneinfo/*/*.ics
%{_datadir}/zoneinfo/*/*/*.ics
