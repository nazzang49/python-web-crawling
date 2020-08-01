import test.v1.bing
import test.v1.unsplash
import test.v2.chrome
import test.v2.naver

if __name__ == "__main__":
    # version 1
    test.v1.do_bing_crawling()
    test.v1.do_unsplash_crawling()

    # version 2
    test.v2.do_chrome_crawling()
    test.v2.do_naver_crawling()