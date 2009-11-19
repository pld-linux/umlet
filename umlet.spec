%define		file_ver	%(echo %{version} | tr . _)
Summary:	Free UML Tool for Fast UML Diagrams
Summary(pl.UTF-8):	Wolnodostępne narzędzie do szybkiego tworzenia diagramów UML
Name:		umlet
Version:	10.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.umlet.com/umlet_10_2/%{name}_%{file_ver}.zip
# Source0-md5:	d9b3ac4d2ac16a770765656589f6aa76
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

%description -l pl.UTF-8
UMLet to narzędzie UML ukierunkowane na szybkie tworzenie diagramów
UML. Elementy UML są modyfikowane poprzez wprowadzanie tekstu zamiast
wyskakujących okien dialogowych. Elementy można modyfikować i używać
jako szablony. W ten sposób użytkownicy mogą łatwo dostosować UMLeta
do swoich potrzeb modelowania. UMLet obsługuje wiele różnych rodzajów
diagramów UML: diagramy klas, diagramy przypadków użycia, diagramy
sekwencji, diagramy stanów, diagramy rozwoju, diagramy aktywności itp.
Co więcej, UMLet pozwala użytkownikom na tworzenie własnych elementów
UML. Wygląd elementu można modyfikować w czasie pracy zmieniając kilka
linii kodu w Javie. Po tym UMLet kompiluje kod nowego elementu w
locie. W ten sposób użytkownicy mogą bez opuszczania UMLeta tworzyć i
dodawać nowe rodzaje elementów do swoich diagramów.

%prep
%setup -q -n UMLet

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
