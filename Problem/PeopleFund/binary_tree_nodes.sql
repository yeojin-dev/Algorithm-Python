SELECT n, IF(p is null, 'Root', IF((SELECT count(*) FROM bst WHERE b.n = p) > 0, 'Inner', 'Leaf')) FROM bst as b ORDER BY n;
