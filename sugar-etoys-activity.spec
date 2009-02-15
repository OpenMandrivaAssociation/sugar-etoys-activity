# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-etoys-activity
Version: 4.0.2205
Release: %mkrel 1
Summary: Squeak Etoys activity for Sugar
License: MIT/Apache
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/etoys/etoys-4.0.2205-2.tar.gz

Requires: sugar-toolkit >= 0.83.6
Requires: squeak-vm-olpc >= 3.10.3

BuildRequires: sugar-toolkit >= 0.83.6
BuildRequires: gettext  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
%setup -q -n etoys-4.0.2205


%build
%configure  \
	--exec-prefix='${prefix}' \
	--datarootdir='${prefix}/share' \
	--datadir='${prefix}/share' \
	--bindir='${prefix}/bin'
make 

%install
rm -rf %{buildroot}
make  \
	ROOT=%{buildroot} \
	datadir=%{buildroot}/%{_prefix}/share \
	install-etoys \
	install-activity

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%dir %{_datadir}/etoys
%{_datadir}/etoys/*
%{_datadir}/mime/packages/*
%{_datadir}/sugar/activities/*
%{_docdir}/*

