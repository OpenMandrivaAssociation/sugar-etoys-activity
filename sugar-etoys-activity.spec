# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-etoys-activity
Version: 116
Release: 1
Summary: Squeak Etoys activity for Sugar
License: MIT/Apache
Group: Graphical desktop/Other
Url: https://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Etoys/Etoys-%{version}.tar.gz

Requires: etoys >= 4.0.2340
Requires: sugar-toolkit >= 0.88.0

BuildRequires: sugar-toolkit >= 0.88.0

BuildArch: noarch

%description
Squeak Etoys was inspired by LOGO, PARC-Smalltalk, Hypercard, starLOGO
and AgentSheets. It is a media-rich authoring environment with a simple,
powerful scripted object model for many kinds of objects created by end-users
that runs on many platforms, and it is free and open source. It includes 2D and
3D graphics, images, text, particles, presentations, web-pages, videos, sound
and MIDI, etc. It includes the ability to share desktops with other Etoy users
in real-time, so many forms of immersive mentoring and play can be done over
the Internet.

%prep
%setup -q -n Etoys-%{version}


%build

rm -f MANIFEST
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f


%files 
%{_datadir}/sugar/activities/*
%doc COPYING NEWS



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 115-2mdv2011.0
+ Revision: 615032
- the mass rebuild of 2010.1 packages

* Sun Apr 04 2010 Aleksey Lim <alsroot@mandriva.org> 115-1mdv2010.1
+ Revision: 531087
- Sucrose 0.88.0 release

* Mon Oct 12 2009 Aleksey Lim <alsroot@mandriva.org> 109-2mdv2010.0
+ Revision: 456975
- Push 109

* Sat Sep 19 2009 Aleksey Lim <alsroot@mandriva.org> 105-2mdv2010.0
+ Revision: 444541
- Update to 105

* Tue Aug 11 2009 Aleksey Lim <alsroot@mandriva.org> 102-1mdv2010.0
+ Revision: 414900
- Sucrose 0.85.2

* Mon Apr 06 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2212-1mdv2009.1
+ Revision: 364293
- Sucrose 0.84.2 release

* Wed Mar 04 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2206-1mdv2009.1
+ Revision: 348317
- Sucrose 0.84.0 release

* Tue Jan 20 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2205-1mdv2009.1
+ Revision: 332035
- new Sucrose 0.83.4 release

* Sat Jan 17 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2201-2mdv2009.1
+ Revision: 330735
- switch build arch to noarch

* Sun Jan 11 2009 Aleksey Lim <alsroot@mandriva.org> 4.0.2201-1mdv2009.1
+ Revision: 328400
- initial commit

