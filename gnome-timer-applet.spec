%define name	gnome-timer-applet
%define version 1.0
%define release 1mdk

Name: 	 	%{name}
Summary: 	Countdown timer applet for the GNOME panel
Version: 	%{version}
Release: 	%{release}

Source:		timer-applet-%{version}.tar.bz2
URL:		http://timerapplet.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libpanel-applet-2-devel

%description
    * Add multiple Timer Applets to the panel to have different timer
      running simultaneously
    * Quickly set a time and the applet will notify you when time's up
    * Create presets for quick access to frequently-used times
    * Small and unobtrusive. Choose to either view the remaining time right
      in the panel or hide it so you don't get distracted by the countdown.
      You can still view the remaining time by hovering your mouse over the
      timer icon
    * User interface follows the GNOME Human Interface Guidelines

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
%{_bindir}/timer-applet
%{_libdir}/bonobo/servers/GNOME_TimerApplet.server
%{_datadir}/gnome/help/timer-applet
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/pixmaps/*
