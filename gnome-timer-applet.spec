%define name	gnome-timer-applet
%define version 2.0.1
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Countdown timer applet for the GNOME panel
Version: 	%{version}
Release: 	%{release}

Source:		timer-applet-%{version}.tar.bz2
URL:		http://timerapplet.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
BuildRequires:	perl-XML-Parser
Requires:	gnome-python >= 2.16
Requires:	gnome-python-desktop >= 2.16
Requires:	python-gnome-glade >= 2.10
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
%setup -q -n timer-applet-%version

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
