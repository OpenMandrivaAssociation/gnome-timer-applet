%define name	gnome-timer-applet
%define version 2.1.4
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Countdown timer applet for the GNOME panel
Version: 	%{version}
Release: 	%{release}

Source:		timer-applet-%{version}.tar.gz
URL:		http://launchpad.net/timer-applet
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	intltool >= 0.35
Requires:	gnome-python >= 2.16
Requires:	gnome-python-desktop >= 2.16
Requires:	pygtk2.0-libglade >= 2.10
Requires:	python-notify >= 0.1
Requires:	dbus-python > 0.80
Requires(post):GConf2
Requires(preun):GConf2

%description
* Quickly set a timer and be notified when it finishes
* Unobtrusive notification that does not interrupt your work, but keeps you
  aware that the timer has finished
* Create presets for quick access to frequently-used times
* Add multiple Timer Applets to the panel to have different timers running
  simultaneously
* D-Bus support provides programmatic access to Timer Applet instances

%prep
%setup -q -n timer-applet

%build
%configure2_5x --disable-schemas-install
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang timer-applet

%post
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/timer-applet.schemas > /dev/null

%preun
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/timer-applet.schemas > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files -f timer-applet.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/timer-applet/timer-applet
%{_libdir}/bonobo/servers/*
%{py_sitedir}/timerapplet
%{_datadir}/timer-applet
%{_datadir}/pixmaps/*


%changelog
* Sat Nov 27 2010 Olivier Faurax <ofaurax@mandriva.org> 2.1.4-1mdv2011.0
+ Revision: 602033
- new home, new version

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 2.0.1-8mdv2011.0
+ Revision: 594852
- rebuild for python 2.7

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.0.1-7mdv2010.0
+ Revision: 437787
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 2.0.1-6mdv2009.1
+ Revision: 325445
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-5mdv2009.0
+ Revision: 240781
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 20 2007 Austin Acton <austin@mandriva.org> 2.0.1-3mdv2008.0
+ Revision: 28953
- fix requires (bug 30923)

* Sun Apr 29 2007 Austin Acton <austin@mandriva.org> 2.0.1-2mdv2008.0
+ Revision: 19212
- buildrequires perl-XML-Parser
- 2.0 python-based version
- Import gnome-timer-applet



* Sun Apr 3 2005 Austin Acton <austin@mandrake.org> 1.0-1mdk
- 1.0
- schemas

* Sat Mar 05 2005 Austin Acton <austin@mandrake.org> 0.7-1mdk
- New release 0.7

* Wed Feb 2 2005 Austin Acton <austin@mandrake.org> 0.5.1-1mdk
- 0.5.1

* Sun Jan 30 2005 Austin Acton <austin@mandrake.org> 0.4-1mdk
- 0.4

* Wed Jan 19 2005 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package
