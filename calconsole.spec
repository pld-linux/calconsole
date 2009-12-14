Summary:	Calconsole - a calendar and schedule in mode command line
Summary(pl.UTF-8):	Calconsole - kalendarz i harmonogram zadań obsługiwany z linii poleceń
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

%description -l pl.UTF-8
Calconsole jest kalendarzem i harmonogramem zadań obsługiwanym z linii
poleceń. Jest podobny do polecenia cal, ale zawiera harmonogram zadań.
Calconsole współpracuje z plikami ics.

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
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/zoneinfo/*/*.ics
%{_datadir}/zoneinfo/*/*/*.ics
