Summary:	A 2D space shooter
Summary(pl.UTF-8):   Kosmiczna strzelanka w 2D
Name:		offender
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/offender/%{name}-%{version}.tar.bz2
# Source0-md5:	05c824b40b4fd416a9eda1c32b651897
URL:		http://offender.sourceforge.net/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Offender is a 2D space shooter a bit like galaga. In it you're one
ship against hundreds of aliens fighting to the death

%description -l pl.UTF-8
Offender jest to strzelanka w 2D podobna do galagi. Gracz kierując
jednym statkiem przeciwko setkom obcych walczy na śmierć i życie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc doc/{AUTHORS,TODO}
%attr(755,root,root) %{_bindir}/%{name}
