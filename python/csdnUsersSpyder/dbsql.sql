use csdn;
CREATE TABLE BlogUser (
        pageID  int(10) unsigned ,
        pageMD5 VARCHAR(64),
        pageUrl varchar(64),
        userName varchar(64),
        follows varchar(512),
        befollowed varchar(512),
        followNum INT,
        befollowedNum INT,
        PRIMARY KEY ( pageID )
);
