# -*- perl -*-

package Bundle::Posy;

=head1 NAME

Bundle::Posy - A bundle to install Posy and plugins

=head1 VERSION

This describes version B<0.50> of Bundle::Posy.

=cut

our $VERSION = '0.50';

=head1 SYNOPSIS

    perl -MCPAN -e 'install Bundle::Posy'

=head1 CONTENTS

Posy - a website generator inspired by blosxom

File::Spec - to make dealing with files more portable

File::stat

File::Find

Storable 2.06 - to store indexes

CGI::Minimal - for CGI with less overhead

Getopt::Long 2.34 - for command-line scripts

Pod::Usage - for command-line scripts

Getopt::ArgvFile 1.09 - for command-line scripts

Posy::Plugin::AntiSpambot - Posy plugin to obfustcate mail links

Posy::Plugin::BinFile - Posy plugin to serve (binary) non-entry files

File::MMagic - find MIME-types of files

Posy::Plugin::Canonical - Posy plugin to force redirect to canonical URL.

Posy::Plugin::Categories - Posy plugin to give category links.

Posy::Plugin::CgiCarp - Posy plugin to aid debugging by using CGI::Carp

CGI::Carp - help CGI debugging

Posy::Plugin::Dump - Posy plugin to aid debugging by dumping object contents

Data::Dumper - dump data

Posy::Plugin::DynamicCss - Posy plugin to load different CSS styles based on the UserAgent.

Posy::Plugin::EntryTitles - Posy plugin to cache entry titles

Posy::Plugin::FileStats - Posy plugin to cache file statistics

Posy::Plugin::FlavourMenu - Posy plugin to make a menu of flavours

Posy::Plugin::LinkExtra - Posy plugin to add extras to local links

Posy::Plugin::LinkList - Posy plugin to give a dynamic list of links

Posy::Plugin::LocalDepth - Posy plugin to filter by local depth

Posy::Plugin::NearLinks - Posy plugin to give links of articles in the current category

Posy::Plugin::Pod - Posy plugin to convert POD files to HTML

Pod::Simple::HTML - convert POD to HTML

Posy::Plugin::RandQuote - Posy plugin to give a random quote from a file

Posy::Plugin::ShortBody - Posy plugin to give the start of an entry body

Posy::Plugin::TextTemplate - Posy plugin for interpolating with Text::Template

Text::Template - templating system which uses Perl as its language

Posy::Plugin::TextToHTML - Posy plugin to convert plain text files to HTML

HTML::TextToHTML 2.34 - to convert text to HTML

Posy::Plugin::ThemeCss - Posy plugin for Cascading Style Sheet themes

Posy::Plugin::ThisFlavour - Posy plugin to change local links to the current flavour

Posy::Plugin::Toc - Posy plugin create a table of contents

Posy::Plugin::YamlConfig - Posy plugin to read config files in YAML format

YAML 0.35 - For YamlConfig

=head1 DESCRIPTION

This bundle includes all the modules used by the Posy website content
management system, and all the major plugins for the Posy system.

A I<Bundle> is a module that simply defines a collection of other
modules.  It is used by the L<CPAN> module to automate the fetching,
building and installing of modules from the CPAN ftp archive sites.

Posy is a website content management system inspired by the design of
blosxom.  The filesystem is the database, there are flavour templates, and
plugins.  However, this system doesn't require one to write one's entry
files in a particular format; one can choose from pure HTML, plain text, or
blosxom format.  And other formats can be dealt with by plugins.

=head1 AUTHOR

    Kathryn Andersen (RUBYKAT)
    perlkat AT katspace dot com
    http://www.katspace.com

=head1 COPYRIGHT AND LICENCE

Copyright (c) 2004-2005 by Kathryn Andersen

This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

=cut

1; # End of Bundle::Posy
__END__
