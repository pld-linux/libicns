#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library for manipulating Macintosh icns files
Summary(pl.UTF-8):	Biblioteka do operowania na plikach icns z Macintosha
Name:		libicns
Version:	0.8.1
Release:	6
Group:		Libraries
# libicns, icns2png and icontainer2icns are under LGPLv2+
# png2icns is under GPLv2+
License:	LGPL v2+ (library and most tools), GPL v2+ (png2icns)
Source0:	http://downloads.sourceforge.net/icns/%{name}-%{version}.tar.gz
# Source0-md5:	7a9b74b84ce08c5b11bdee3cad296dd3
URL:		http://icns.sourceforge.net/
BuildRequires:	jasper-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libicns is a library providing functionality for easily reading and
writing Macintosh icns files.

%description -l pl.UTF-8
libicns to biblioteka umożliwiająca łatwy odczyt i zapis plików icns z
Macintosha.

%package devel
Summary:	Development files for libicns library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libicns
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libicns.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libicns.

%package static
Summary:	Static libicns library
Summary(pl.UTF-8):	Statyczna biblioteka libicns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libicns library.

%description static -l pl.UTF-8
Statyczna biblioteka libicns.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libicns.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/icns2png
%attr(755,root,root) %{_bindir}/icontainer2icns
%attr(755,root,root) %{_bindir}/png2icns
%attr(755,root,root) %{_libdir}/libicns.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libicns.so.1
%{_mandir}/man1/icns2png.1*
%{_mandir}/man1/icontainer2icns.1*
%{_mandir}/man1/png2icns.1*

%files devel
%defattr(644,root,root,755)
%doc src/apidocs.html
%attr(755,root,root) %{_libdir}/libicns.so
%{_includedir}/icns.h
%{_pkgconfigdir}/libicns.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libicns.a
%endif
