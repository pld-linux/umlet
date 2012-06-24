Summary:	Free UML Tool for Fast UML Diagrams
Summary(pl):	Wolnodost�pne narz�dzie do szybkiego tworzenia diagram�w UML
Name:		umlet
Version:	6
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.umlet.com/umlet_6/%{name}%{version}.zip
# Source0-md5:	8e97ebae438ee2dd8130df20d50db166
URL:		http://www.umlet.com/
BuildRequires:	unzip
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UMLet is a UML tool aimed at providing a fast way of creating UML
diagrams. UML elements are modified using text input instead of pop-up
dialogs. Elements can be modified and used as templates. This way,
users can easily tailor UMLet to their modeling needs. UMLet supports
a variety of UML diagram types: class diagrams, use case diagrams,
sequence diagrams, state diagrams, deployment diagrams, activity
diagrams, etc. Furthermore, UMLet allows users to create their own
custom UML elements. An element's look can be modified at run-time by
changing a few lines of Java code. UMLet then compiles the new
element's code on the fly. Without leaving UMLet, users can thus
create and add new element types to their diagrams.

%description -l pl
UMLet to narz�dzie UML ukierunkowane na szybkie tworzenie diagram�w
UML. Elementy UML s� modyfikowane poprzez wprowadzanie tekstu zamiast
wyskakuj�cych okien dialogowych. Elementy mo�na modyfikowa� i u�ywa�
jako szablony. W ten spos�b u�ytkownicy mog� �atwo dostosowa� UMLeta
do swoich potrzeb modelowania. UMLet obs�uguje wiele r�nych rodzaj�w
diagram�w UML: diagramy klas, diagramy przypadk�w u�ycia, diagramy
sekwencji, diagramy stan�w, diagramy rozwoju, diagramy aktywno�ci itp.
Co wi�cej, UMLet pozwala u�ytkownikom na tworzenie w�asnych element�w
UML. Wygl�d elementu mo�na modyfikowa� w czasie pracy zmieniaj�c kilka
linii kodu w Javie. Po tym UMLet kompiluje kod nowego elementu w
locie. W ten spos�b u�ytkownicy mog� bez opuszczania UMLeta tworzy� i
dodawa� nowe rodzaje element�w do swoich diagram�w.

%prep
%setup -q -n com.%{name}.plugin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cat > $RPM_BUILD_ROOT%{_bindir}/umlet <<EOF
#!/bin/sh
cwd=\`pwd\`
cd %{_datadir}/%{name}
java -jar umlet.jar
cd \$cwd
EOF

cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/custom_elements
%{_datadir}/%{name}/icons
# lib contains jars.
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/palettes
%{_datadir}/%{name}/*.jar
