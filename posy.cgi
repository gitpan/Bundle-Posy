#!/usr/bin/perl -T
# vim:ts=8 sw=4 sts=4 ai
require v5.6.1;
$ENV{PATH} ="/bin:/usr/bin:/usr/local/bin";
delete @ENV{ 'IFS', 'CDPATH', 'ENV', 'BASH_ENV'};
use strict;

=head1 NAME

posy.cgi - CGI script using the Posy website generator

=head1 VERSION

This describes version B<0.70> of posy.cgi.

=cut

our $VERSION = '0.70';

=head1 SYNOPSIS

posy.cgi?path=/reviews/movies/

posy.cgi/reviews/movies/

=head1 DESCRIPTION

CGI script using the Posy web content manager.

This version right here is set up to use all the core plugins, and has a more
complicated (and more portable) way of setting the directory variables.

=head1 INSTALLATION

=head2 Installation

First of all, install the Posy module.  (See the Posy documentation)
If you were forced to install Posy somewhere non-standard, make
note of the location.  You will need this for the configuration.

Then you need to put this script in your cgi-bin directory on your website.
You may have to edit the first line if the perl program is in a different
location.  Make the posy.cgi script executable.

Create your data directory; make note of its location.

=head2 Configuration

For simplicity's sake, the initial configuration settings for posy
are held in this script itself.  Some are essential, some can be
left at the default.

Essential:

=over

=item libdir

If you installed the Posy module in a non-standard place, then
you need to tell this script where to look for it.  Set $libdir
to that directory.

For example, if the Posy.pm module is in
/home/fred/perl/lib
(that is, its full path is /home/fred/perl/lib/Posy.pm)
then

    $libdir = '/home/fred/perl/lib';

This assumes that any Posy plugins are also under the same directory.

=cut

our $basedir;
our $libdir;
BEGIN {
    use File::Spec;
    # untaint DOCUMENT_ROOT
    $ENV{DOCUMENT_ROOT} =~ m#^([-._/\w]+)$#;
    my $doc_root = $1;
    my @dd = File::Spec->splitdir($doc_root);
    pop @dd;
    push @dd, 'data';
    $basedir = File::Spec->catdir(@dd);
    $libdir = "$basedir/lib";
}

=item data_dir

Where are this site's entries kept?

$data_dir = '/files/www/posy/docs';

=cut

our $data_dir = "$basedir/docs";

=back

Optional:

=over

=item url

What is my preferred base URL for this site/blog?  (leave unset for
automatic)

    my $url = 'http://www.example.com/blog/';

=cut

our $url = '';

=item flavour_dir

The directory where "flavour" template files are put.
The default value is ".flavours" under the data directory.

$flavour_dir = "/files/www/posy/flavours";

=cut
our $flavour_dir = "$basedir/flavours";

=item config_dir

If you want your config files to be in a different
directory to the data directory, then change this value.

=cut
our $config_dir = $data_dir;

=item plugins

If you wish to use any plugins, you must put them in the plugins list,
as well as installing the actual plugin modules.

For example, if you are using the Posy::Plugin::TextTemplate module,
then the TextTemplate.pm file should either be installed using
the standard Build method, or you should just put the TextTemplate.pm
file in the Posy/Plugin directory under Posy.pm

That is, if Posy.pm is in /home/fred/perl/lib/, then
TextTemplate.pm should be in /home/fred/perl/lib/Posy/Plugin/

Then you add the name of the plugin to this plugins list.
Always put Posy::Core first.

    my @plugins = qw(Posy::Core Posy::Plugin::TextTemplate);

Remember that the order of plugins in the list is important if two
plugins override the same function.

=cut

our @plugins = qw(Posy::Core
    Posy::Plugin::TextTemplate
    Posy::Plugin::TextToHTML
    Posy::Plugin::YamlConfig
    Posy::Plugin::Canonical
    Posy::Plugin::FindGrep
    Posy::Plugin::EntryTitles
    Posy::Plugin::Pod
    Posy::Plugin::FileStats
    Posy::Plugin::DynamicCss
    Posy::Plugin::Paginate
    Posy::Plugin::ThemeCss
    Posy::Plugin::FlavourMenu
    Posy::Plugin::LinkList
    Posy::Plugin::Categories
    Posy::Plugin::LocalDepth
    Posy::Plugin::ShortBody
    Posy::Plugin::AntiSpambot
    Posy::Plugin::RandQuote
    Posy::Plugin::ThisFlavour
    Posy::Plugin::LinkExtra
    Posy::Plugin::Toc
    Posy::Plugin::NearLinks
    Posy::Plugin::BinFile
    Posy::Plugin::NotFound
    );

=item file_extensions

If you wish to change the default file extensions, then set this.
Generally one would only do this if one had added a plugin to deal
with a new kind of file, or if you want to use a different extension
for a standard type of file.
 
    our %file_extensions = (
	txt=>'text',
	html=>'html',
	blx=>'blosxom',
	);

=cut

our %file_extensions = (
	txt=>'text',
	html=>'html',
	blx=>'blosxom',
	pl=>'pod',
	pm=>'pod',
	pod=>'pod',
	);

=item actions

The list of actions which Posy will perform.  Only alter this if you're using
a plugin which requires adding a new action.

=cut

our @actions = qw(init_params
	    parse_path
	    set_config
	    process_path_error
	    anti_spambot_show_mail
	    index_entries
	    index_file_stats
	    index_titles
	    select_by_path
	    filter_by_date
	    filter_by_localdepth
	    sort_entries
	    filter_by_page
	    content_type
	    head_template
	    foot_template
	    dynamic_css_set
	    theme_css_set
	    flavour_menu_set
	    findgrep_set
	    head_render
	    do_entry_actions
	    foot_render
	    render_page
	);

=item entry_actions

The list of actions which Posy will perform on each entry.  Only alter this if
you're using a plugin which requires adding a new entry action.

=cut

our @entry_actions = qw(
	    count_or_stop
	    read_entry
	    parse_entry
	    head_render
	    header
	    entry_template
	    short_body
	    anti_spambot_obscure_mail
	    rand_quote
	    link_extra
	    this_flavour
	    make_toc
	    render_entry
	    append_entry
	    foot_render
	);

=item DayWeek2Name

This is a hash which sets how a day-of-the-week number will be
converted into a name.  Change this if you want, for example,
all weekdays to be truncated, or in another language.

=cut
our %DayWeek2Name = ( 0 => 'Sunday',
	    1 => 'Monday',
	    2 => 'Tuesday',
	    3 => 'Wednesday',
	    4 => 'Thursday',
	    5 => 'Friday',
	    6 => 'Saturday');

=item MonthNum2Name

This is a hash which sets how a month-number will be
converted into a name.  Change this if you want, for example,
all month-names to be truncated, or in another language.

=cut
our %MonthNum2Name = (1=>'January',
	    2=>'February',
	    3=>'March',
	    4=>'April',
	    5=>'May',
	    6=>'June',
	    7=>'July',
	    8=>'August',
	    9=>'September',
	    10=>'October',
	    11=>'November',
	    12=>'December'
	);

=item state_dir

The directory where "state" information is put.  The default value is
".state" under the data directory).

=cut

our $state_dir = "$basedir/state";

=back

=head1 REQUIRES

    Posy

=head1 SEE ALSO

perl(1)
Posy

=cut

#========================================================
# Subroutines

#========================================================
# Main

use lib "$libdir";
my $class='Posy';
eval "require $class;";
die "invalid starter class $class: $@" if $@;

$class->import(@plugins);

my %run_args = (
		data_dir=>$data_dir,
		flavour_dir=>$flavour_dir,
		config_dir=>$config_dir,
		state_dir=>$state_dir,
		DayWeek2Name=>\%DayWeek2Name,
		MonthNum2Name=>\%MonthNum2Name,
		debug_level=>0,
	       );
# set the other options, if they exist
$run_args{url} = $url if defined $url;
$run_args{file_extensions} = \%file_extensions if %file_extensions;
$run_args{actions} = \@actions if @actions;
$run_args{entry_actions} = \@entry_actions if @entry_actions;

$class->run(%run_args);

=head1 BUGS

Please report any bugs or feature requests to the author.

=head1 AUTHOR

    Kathryn Andersen (RUBYKAT)
    perlkat AT katspace dot com
    http://www.katspace.com

=head1 COPYRIGHT AND LICENCE

Copyright (c) 2004-2005 by Kathryn Andersen

This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.


=cut

__END__