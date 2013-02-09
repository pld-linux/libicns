Summary:	Library for manipulating Macintosh icns files
Name:		libicns
Version:	0.8.1
Release:	1
Group:		Libraries
# libicns, icns2png and icontainer2icns are under LGPLv2+
# png2icns is under GPLv2+
License:	LGPL v2+ and GPL v2+
URL:		http://icns.sourceforge.net/
Source0:	http://downloads.sourceforge.net/icns/%{name}-%{version}.tar.gz
# Source0-md5:	7a9b74b84ce08c5b11bdee3cad296dd3
BuildRequires:	jasper-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libicns is a library providing functionality for easily reading and
writing Macintosh icns files.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static

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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/icns2png
%attr(755,root,root) %{_bindir}/icontainer2icns
%attr(755,root,root) %{_bindir}/png2icns
%attr(755,root,root) %{_libdir}/libicns.so.*.*.*
%ghost %{_libdir}/libicns.so.1
%{_mandir}/man1/icns2png.1*
%{_mandir}/man1/icontainer2icns.1*
%{_mandir}/man1/png2icns.1*

%files devel
%defattr(644,root,root,755)
%doc src/apidocs.*
%{_includedir}/icns.h
%{_libdir}/libicns.so
%{_pkgconfigdir}/%{name}.pc
