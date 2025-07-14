%define		subver rc2
%define		rel 1
Summary:	libmemcache - the C API for memcached
Summary(pl.UTF-8):	libmemcache - API C do memcached
Name:		libmemcache
Version:	1.4.0
Release:	0.%{subver}.%{rel}
License:	MIT
Group:		Libraries
Source0:	http://people.freebsd.org/~seanc/libmemcache/%{name}-%{version}.%{subver}.tar.bz2
# Source0-md5:	402c957cd71538c07a263542eeb513d1
Patch0:		%{name}-make.patch
URL:		http://people.freebsd.org/~seanc/libmemcache/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Features:
- Support for Multiple Memory Contexts. This is primarily used for
  programs that need to use memcache(3) inside of Apache where both
  Apache and PHP have their own memory management systems.
- Callback Interface. Using the callback interface, it's possible to
  lump many gets together into a single get request with a great deal of
  ease.
- Multiple Client Side Hashes. memcache(3) supports multiple hashing
  methods to distribute load across multiple servers.
- Multiple Servers. memcache(3) supports multiple servers.
- Support for Garbage Collection. memcache(3) was written with the
  Boehm Garbage Collector in mind.
- MIT Licensed. memcache(3) is as Open Source as it gets and can be
  embedded in anything (commercial software, open source, etc).

%description -l pl.UTF-8
Możliwości:
- Obsługa wielu kontekstów pamięci; służy głównie do programów, które
  muszą używać memcache(3) wewnątrz Apache'a, gdzie zarówno Apache jak i
  PHP mają własne systemy zarządzania pamięcią.
- Interfejs wywołań zwrotnych; przy jego użyciu można pogodzić wiele
  pobrań w jedno żądanie pobrania znacznie ułatwiając pracę.
- Wiele haszy po stronie klienta; memcache(3) obsługuje wiele metod
  haszowania do rozdysponowania obciążenia na wiele serwerów.
- Wiele serwerów; memcache(3) obsługuje wiele serwerów.
- Obsluga odśmiecacza; memcache(3) zostało napisane z myślą o Boehm
  Garbage Collectorze.
- Licencja MIT; memcache(3) to oprogramowanie z otwartymi źródłami,
  które można osadzić gdziekolwiek (w programowaniu komercyjnym, open
  source itd.).

%package devel
Summary:	Header files for libmemcache library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmemcache
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libmemcache.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libmemcache.

%package static
Summary:	Static libmemcache library
Summary(pl.UTF-8):	Statyczna biblioteka libmemcache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmemcache library.

%description static -l pl.UTF-8
Statyczna biblioteka libmemcache.

%prep
%setup -q -n %{name}-%{version}.%{subver}
%patch -P0 -p1

# create tests dir without Makefiles
cp -a test tests
rm -f tests{,/*}/Makefile*

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog INSTALL
%attr(755,root,root) %{_libdir}/libmemcache.so.*.*

%files devel
%defattr(644,root,root,755)
%doc tests/
%attr(755,root,root) %{_libdir}/libmemcache.so
%{_libdir}/libmemcache.la
%{_includedir}/memcache
%{_includedir}/memcache.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmemcache.a
