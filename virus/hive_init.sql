CREATE TABLE `feiyan_track_info`(
  `city` string,
  `confid` string,
  `contact` string,
  `contact_detail` string,
  `county` string,
  `hashtag` string,
  `lasttime` string,
  `location` string,
  `other_info` string,
  `province` string,
  `pub_time` string,
  `source` string,
  `source_url` string,
  `track` string,
  `user_name` string,
  `user_num` string)
  partitioned by (dt string)STORED AS orc;


  CREATE TABLE `province_city_mapping`(
  `city` string,
  `city_name_alias` string,
  `province` string,
  `province_pin_yin` string)
    partitioned by (dt string)STORED AS orc;


CREATE TABLE `city_feiyan_info`(
  `city` string,
  `confirm` bigint,
  `confirm_add` string,
  `date` string,
  `dead` bigint,
  `heal` bigint,
  `suspect` bigint,
  `y` string) partitioned by (dt string)STORED AS orc;


  CREATE TABLE `foreign_feiyan_info`(
  `confirm` bigint,
  `confirm_add` bigint,
  `continent` string,
  `country` string,
  `date` string,
  `dead` bigint,
  `heal` bigint,
  `y` string)
  partitioned by (dt string)STORED AS orc;


CREATE TABLE `province_feiyan_info`(
  `confirm` bigint,
  `confirm_add` string,
  `confirm_cuts` string,
  `country` string,
  `date` string,
  `dead` bigint,
  `dead_cuts` string,
  `description` string,
  `heal` bigint,
  `heal_cuts` string,
  `newconfirm` bigint,
  `newdead` bigint,
  `newheal` bigint,
  `now_confirm_cuts` string,
  `province` string,
  `wzz` bigint,
  `wzz_add` bigint,
  `year` bigint)
    partitioned by (dt string)STORED AS orc;
