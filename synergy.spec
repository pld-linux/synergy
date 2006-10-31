Summary:	Mouse and keyboard sharing utility
Name:		synergy
Version:	1.3.1
Release:	0.1
License:	GPL
Group:		Daemons
URL:		http://synergy2.sourceforge.net/
Source0:	http://dl.sourceforge.net/synergy2/%{name}-%{version}.tar.gz
# Source0-md5:	a6e09d6b71cb217f23069980060abf27
BuildRequires:	X11-devel
#BuildRequires:	libX11-devel
#BuildRequires:	libXext-devel
#BuildRequires:	libXinerama-devel
#BuildRequires:	libXt-devel
#BuildRequires:	libXtst-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING doc/PORTING NEWS README
%doc doc/*.css doc/*.html
%doc examples/synergy.conf
%attr(755,root,root) %{_bindir}/synergyc
%attr(755,root,root) %{_bindir}/synergys
