

CREATE TABLE `photoAlbums` (
  `albumID` int(11) NOT NULL auto_increment,
  `albumName` varchar(220) default NULL,
  `albumCreateDate` date default NULL,
  `albumModifiedDate` date default NULL,
  `albumParentID` int(11) unsigned default NULL,
  `albumFriendlyName` text,
  `albumDesc` text,
  PRIMARY KEY  (`albumID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;




CREATE TABLE `photoComments` (
  `commentID` int(11) NOT NULL auto_increment,
  `commentContent` text,
  `commentPhotoID` int(11) NOT NULL,
  PRIMARY KEY  (`commentID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



# Dump of table photoLibrary
# ------------------------------------------------------------


CREATE TABLE `photoLibrary` (
  `photoID` int(11) NOT NULL auto_increment,
  `photoTitle` text,
  `photoDesc` text,
  `photoFileName` text,
  `photoCreatedDate` date default NULL,
  `photoAlbumID` int(11) NOT NULL,
  `isProfilePic` int(11) default '0',
  PRIMARY KEY  (`photoID`)
) ENGINE=MyISAM AUTO_INCREMENT=103 DEFAULT CHARSET=utf8;


CREATE TABLE `photoSessions` (
  `session_id` varchar(40) NOT NULL default '0',
  `ip_address` varchar(16) NOT NULL default '0',
  `user_agent` varchar(50) NOT NULL,
  `last_activity` int(10) unsigned NOT NULL default '0',
  `user_data` text NOT NULL,
  PRIMARY KEY  (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;





CREATE TABLE `photoSettings` (
  `settingID` int(11) default NULL,
  `settingName` varchar(255) default NULL,
  `settingValue` varchar(255) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO `photoSettings` (`settingID`,`settingName`,`settingValue`)
VALUES
	(1,'siteName','Coolest photo album ever'),
	(2,'siteTheme','0'),
	(3,'absoluteFilePath','/home/content/d/s/t/dstegelman/html/code/snapit/'),
	(4,'enableOriginalDownload','TRUE'),
	(5,'userTable','photoUsers'),
	(6,'libraryTable','photoLibrary'),
	(7,'albumTable','photoAlbums'),
	(8,'commentTable','photoComments'),
	(9,'versionNumber','0.1.2'),
	(10,'enableComments','FALSE'),
	(11,'enableSlideshow','TRUE'),
	(12,'debugMode','FALSE'),
	(13,'enableMaps','FALSE'),
	(14,'enablePhotoInfo','FALSE'),
	(15,'enableLiveEdit','TRUE'),
	(16,'enableFullViewPhoto','TRUE'),
	(17,'enablePhotoFTPImport','FALSE'),
	(18,'enableUserCreation','TRUE'),
	(19,'planType','0'),
        (20, 'useShadowbox', 'TRUE'),
        (21, 'showPhotoTitle', 'TRUE');


CREATE TABLE `photoUsers` (
  `userID` int(11) NOT NULL auto_increment,
  `email` varchar(45) default NULL,
  `pass` varchar(255) default NULL,
  `firstName` varchar(255) default NULL,
  `lastName` varchar(255) default NULL,
  `dateCreated` date default NULL,
  PRIMARY KEY  (`userID`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;