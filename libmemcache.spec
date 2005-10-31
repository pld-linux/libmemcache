Summary:	libmemcache - the C API for memcached
Summary(pl):	libmemcache - API C do memcached
Name:		libmemcache
Version:	1.4.0
%define		_beta	9
%define		_rel 1
Release:	0.beta%{_beta}.%{_rel}
Epoch:		0
License:	MIT
Group:		Libraries
Source0:	http://people.freebsd.org/~seanc/libmemcache/%{name}-%{version}.b%{_beta}.tar.bz2
# Source0-md5:	0e003d5dfbc6e59ec400019507f9a61d
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

%description -l pl
Mo¿liwo¶ci:
- Obs³uga wielu kontekstów pamiêci; s³u¿y g³ównie do programów, które
  musz± u¿ywaæ memcache(3) wewn±trz Apache'a, gdzie zarówno Apache jak
  i PHP maj± w³asne systemy zarz±dzania pamiêci±.
- Interfejs wywo³añ zwrotnych; przy jego u¿yciu mo¿na pogodziæ wiele
  pobrañ w jedno ¿±danie pobrania znacznie u³atwiaj±c pracê.
- Wiele haszy po stronie klienta; memcache(3) obs³uguje wiele metod
  haszowania do rozdysponowania obci±¿enia na wiele serwerów.
- Wiele serwerów; memcache(3) obs³uguje wiele serwerów.
- Obsluga od¶miecacza; memcache(3) zosta³o napisane z my¶l± o Boehm
  Garbage Collectorze.
- Licencja MIT; memcache(3) to oprogramowanie z otwartymi ¼ród³ami,
  które mo¿na osadziæ gdziekolwiek (w programowaniu komercyjnym, open
  source itd.).

%package devel
Summary:	Header files for libmemcache library
Summary(pl):	Pliki nag³ówkowe biblioteki libmemcache
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libmemcache.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki libmemcache.

%package static
Summary:	Static libmemcache library
Summary(pl):	Statyczna biblioteka libmemcache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmemcache library.

%description static -l pl
Statyczna biblioteka libmemcache.

%prep
%setup -q -n %{name}-%{version}.b%{_beta}
%patch0 -p1

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

%{__make} -j1 install \
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
