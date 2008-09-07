%define major	2
%define libname	%mklibname nova %{major}
%define develname %mklibname nova -d

Name:       libnova
Version:    0.12.2
Release:    %mkrel 2
Summary:    General purpose astronomy & astrodynamics library
Group:      Sciences/Astronomy
License:    LGPLv2+
URL:        http://sourceforge.net/projects/libnova/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   %{libname} = %{version}-%{release}

%description
Libnova is a general purpose, double precision, celestial mechanics, 
astrometry and astrodynamics library

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc ChangeLog README AUTHORS NEWS COPYING
%{_bindir}/libnovaconfig


#--------------------------------------------------------------------

%package -n %{libname}
Summary:    Library files for %name
Group:      Development/KDE and Qt

%description -n %{libname}
Contains library files for nova

%files -n %{libname}
%{_libdir}/libnova-0.12.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:    Development files for %name
Group:      Development/KDE and Qt
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Contains library and header files for %nova

%files -n %{develname}
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
