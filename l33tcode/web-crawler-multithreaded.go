package main

import (
	"math/rand"
	"strings"
	"sync"
	"time"
)

/*
 This is HtmlParser's API interface.
 You should not implement it, or speculate about its implementation
    type HtmlParser struct {
        maps  map[string]int
        imaps map[int]string
        a     map[int][]int
    }
*/

var (
	wg      sync.WaitGroup
	visited sync.Map
)

func fetch(domain string, url string, htmlParser *HtmlParser) {
	defer wg.Done()

	_, loaded := visited.LoadOrStore(url, struct{}{})
	if loaded {
		return
	}

	urls := htmlParser.GetUrls(url)

	for _, nextURL := range urls {
		nextDomain := strings.Split(nextURL, "/")[2]
		if nextDomain != domain {
			continue
		}

		wg.Add(1)
		go fetch(domain, nextURL, htmlParser)
	}
}

func crawl(startUrl string, htmlParser *HtmlParser) []string {
	wg = sync.WaitGroup{}
	visited = sync.Map{}

	domain := strings.Split(startUrl, "/")[2]

	wg.Add(1)
	go fetch(domain, startUrl, htmlParser)

	wg.Wait()

	urls := []string{}

	visited.Range(func(key, value any) bool {
		urls = append(urls, key.(string))
		return true
	})

	return urls
}
