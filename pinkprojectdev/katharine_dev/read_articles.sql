select a.article_url
from article_rec as a
join word_frequency_rec as f
on a.article_id = f.article_id
join word_rec as w on f.word_id = w.word_id
where word='%s'
order by frequency DESC;
