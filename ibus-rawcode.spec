Name:       ibus-rawcode
Version:    1.3.2
Release:    1%{?dist}
Summary:    The Rawcode engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        https://fedorahosted.org/ibus-rawcode/
Source0:    https://fedorahosted.org/releases/i/b/ibus-rawcode/%{name}-%{version}.tar.gz

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel


Requires:   ibus

%description
The Rawcode engine for IBus platform.

%prep
%setup -q

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{python_sitearch}/_rawcode.la

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-rawcode
%{_datadir}/ibus-rawcode
%{_datadir}/ibus/component/*

%changelog
* Wed Mar 27 2013 Pravin Satpute <psatpute@redhat.com> - 1.3.2-1
- configured with autoconf 2.69

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1.20100707-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> - 1.3.1.20100707-9
- spec file cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1.20100707-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Pravin Satpute <psatpute@redhat.com> - 1.3.1.20100707-7
- rebuild for broken dependancies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1.20100707-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Pravin Satpute <psatpute@redhat.com> - 1.3.1.20100707-5
- Resolved bug #741189

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1.20100707-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.1.20100707-3
- rebuild for broken dependancies

* Wed Jul 07 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.1.20100707-1
- upstream new release
- fixed bug 612042

* Fri Jun 11 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100421-2
- added auxiliary text support, for space hit
- fixed bug 602942

* Wed Apr 21 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100421-1
- upstream new release
- fixed bug 584233, 584240 

* Mon Feb 08 2010 Adam Jackson <ajax@redhat.com> 1.2.99.20100208-2
- Rebuild for new libibus.so.2 ABI.

* Mon Feb 08 2010 Pravin Satpute <pravin.d.s@gmail.com> - 1.2.99.20100208-1
- updated patches for code enhancements from phuang for ibus-1.2.99
- new upstream release

* Fri Dec 11 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-4
- resolved bug 546521

* Tue Nov 17 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-3
- resolved bug 531989

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-1
- upstream release 1.2.0

* Sun Jun 28 2009 Matthias Clasen <mclasen@redhat.com> - 1.0.0.20090303-3
- Rebuild against newer ibus

* Tue Mar 03 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090303-2
- removed mod_path
- added build requires ibus-devel

* Tue Mar 03 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090303-1
- The first version.
