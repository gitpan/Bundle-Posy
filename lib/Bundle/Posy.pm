# -*- perl -*-

package Bundle::Posy;

=head1 NAME

Bundle::Posy - A bundle to install Posy and plugins

=head1 VERSION

This describes version B<0.70> of Bundle::Posy.

=cut

our $VERSION = '0.70';

=head1 SYNOPSIS

    perl -MCPAN -e 'install Bundle::Posy'

=head1 CONTENTS

Posy - a website generator inspired by blosxom

Posy::Plugin::AntiSpambot - Posy plugin to obfustcate mail links

Posy::Plugin::BinFile - Posy plugin to serve (binary) non-entry files

Posy::Plugin::Canonical - Posy plugin to force redirect to canonical URL.

Posy::Plugin::Categories - Posy plugin to give category links.

Posy::Plugin::CgiCarp - Posy plugin to aid debugging by using CGI::Carp

Posy::Plugin::Dump - Posy plugin to aid debugging by dumping object contents

Posy::Plugin::DynamicCss - Posy plugin to load different CSS styles based on the UserAgent.

Posy::Plugin::EntryTitles - Posy plugin to cache entry titles

Posy::Plugin::FileStats - Posy plugin to cache file statistics

Posy::Plugin::FindGrep - Posy plugin to find files using grep.

Posy::Plugin::FlavourMenu - Posy plugin to make a menu of flavours

Posy::Plugin::LinkExtra - Posy plugin to add extras to local links

Posy::Plugin::LinkList - Posy plugin to give a dynamic list of links

Posy::Plugin::LocalDepth - Posy plugin to filter by local depth

Posy::Plugin::NearLinks - Posy plugin to give links of articles in the current category

Posy::Plugin::NotFound - Posy plugin to provide a custom Not Found page.

Posy::Plugin::Paginate - Posy plugin to paginate multiple entries.

Posy::Plugin::Pod - Posy plugin to convert POD files to HTML

Posy::Plugin::RandQuote - Posy plugin to give a random quote from a file

Posy::Plugin::ShortBody - Posy plugin to give the start of an entry body

Posy::Plugin::TextTemplate - Posy plugin for interpolating with Text::Template

Posy::Plugin::TextToHTML - Posy plugin to convert plain text files to HTML

Posy::Plugin::ThemeCss - Posy plugin for Cascading Style Sheet themes

Posy::Plugin::ThisFlavour - Posy plugin to change local links to the current flavour

Posy::Plugin::Toc - Posy plugin create a table of contents

Posy::Plugin::YamlConfig - Posy plugin to read config files in YAML format

=head1 DESCRIPTION

This bundle includes all the modules used by the Posy website content
management system, and all the major plugins for the Posy system.
It does NOT include the modules upon which they depend.

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
