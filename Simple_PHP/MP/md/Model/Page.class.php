<?php
	//分页类
	class Page extends DB{
		//属性

		//方法
		/*
		 * 分页方法
		 * @param1 string $url 当前页面url
		 * @param2 int $pages总记录数
		 * @param4 int $page当前页数
		 * @return string $str 返回一个带分页链接的字符串
		*/
		public static function showpages($url,$pages,$page = 1){
			//设置每页显示记录数
			$pagesize = $GLOBALS['config']['pagesize'];
			//求出总页数
			$pageCounts = ceil($pages / $pagesize);
			//如果页数为0 返回空
			if($pageCounts == 0 ) return '';
			//计算上一页和下一页
			$prev = ($page == 1) ? $page : ($page - 1);
			$next = ($page == $pageCounts) ? $pageCounts : ($page + 1);

			
			//构建返回字符串
			$str = <<<ENDPAGE
				<span id="str_page">
				总共有"{$pages}"条记录&nbsp;&nbsp;每页显示"{$pagesize}"条&nbsp;&nbsp;
				<a href="{$url}&page=1">首页</a>&nbsp;&nbsp;
				<a href="{$url}&page={$prev}">上一页</a>&nbsp;&nbsp;
				<a href="{$url}&page={$next}">下一页</a>&nbsp;&nbsp;
				<a href="{$url}&page={$pageCounts}">末页</a>&nbsp;&nbsp;
				</span>
ENDPAGE;
			return $str;
		}
		
	}

?>