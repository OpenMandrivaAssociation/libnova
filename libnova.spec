Name:       libnova
Version:    0.12.1
Release:    %mkrel 1
Summary:    General purpose astronomy & astrodynamics library
Group:      Sciences/Astronomy
License:    LGPLv2+
URL:        http://sourceforge.net/projects/libnova/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libnova is a general purpose, double precision, celestial mechanics, 
astrometry and astrodynamics library

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog README AUTHORS NEWS COPYING
%{_libdir}/libnova-0.12.so.1.0.0
%{_libdir}/libnova-0.12.so.1
%{_bindir}/libnovaconfig

#--------------------------------------------------------------------

%package devel
Summary:    Development files for %name
Group:      Development/KDE and Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Contains library and header files for %nova

%files devel
%doc COPYING examples/*.c
%{_includedir}/libnova
%{_libdir}/libnova.so

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure --disable-static
make CFLAGS="$RPM_OPT_FLAGS"  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT
