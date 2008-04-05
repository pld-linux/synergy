Summary:	Mouse and keyboard sharing utility
Summary(pl.UTF-8):	Narzędzie do dzielenia myszy i klawiatury
Name:		synergy
Version:	1.3.1
Release:	2
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/synergy2/%{name}-%{version}.tar.gz
# Source0-md5:	a6e09d6b71cb217f23069980060abf27
Source1:	%{name}-client.init
Source2:	%{name}-client.conf
Source3:	%{name}-server.init
Source4:	%{name}-server.conf
Source5:	%{name}-server-layout.conf
URL:		http://synergy2.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%description -l pl.UTF-8
Synergy pozwala łatwo i bez specjalnego sprzętu dzielić jedną mysz i
klawiaturę pomiędzy wiele komputerów z różnymi systemami operacyjnymi,
z których każdy ma własny monitor. Jest przeznaczony dla użytkowników
z wieloma komputerami na biurku, jako że każdy system używa własnego
monitora.

%package xinitrc-client
Summary:	xinitrc startup scripts for synergy client
Summary(pl.UTF-8):	Skrypty startowe xinitrc dla klienta synergy
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	xinitrc

%description xinitrc-client
xinitrc startup scripts for synergy client.

%description xinitrc-client -l pl.UTF-8
Skrypty startowe xinitrc dla klienta synergy.

%package xinitrc-server
Summary:	xinitrc startup scripts for synergy server
Summary(pl.UTF-8):	Skrypty startowe xinitrc dla serwera synergy
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	xinitrc

%description xinitrc-server
xinitrc startup scripts for synergy server.

%description xinitrc-server -l pl.UTF-8
Skrypty startowe xinitrc dla serwera synergy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{X11/xinit/xinitrc.d,synergy}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/synergyc.sh
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/client.conf

install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/synergys.sh
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/server.conf

install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/synergy/layout.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING doc/PORTING NEWS README
%doc doc/*.css doc/*.html
%doc examples/synergy.conf
%attr(755,root,root) %{_bindir}/synergyc
%attr(755,root,root) %{_bindir}/synergys
%dir %{_sysconfdir}/synergy

%files xinitrc-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/synergyc.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/client.conf

%files xinitrc-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/synergys.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/server.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/synergy/layout.conf
