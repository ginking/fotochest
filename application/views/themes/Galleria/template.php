<!DOCTYPE html>
<html>
	<head>
		
                <?php echo theme_css('styles'); ?>
                <?php echo getJquery(); ?>
                <?php echo js('fotochest'); ?>
		<link href='http://fonts.googleapis.com/css?family=Cuprum&subset=latin' rel='stylesheet' type='text/css'>
		<title><?php echo $title; ?></title>
	</head>
	<body>
		<div id="wrapper">
		<a class="logo" href="<?php echo site_url(); ?>">
		foto<span>chest</span>
		</a>

                <?php echo $content; ?>

                </div>
        </body>
</html>

