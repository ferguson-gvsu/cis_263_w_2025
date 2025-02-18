rm(list = ls())

library(ggplot2)

df_bogosort = read.csv('data_bogosort.csv')
df_bogosort$sort = 'bogo'

df_bubble = read.csv('data_bubble_sort.csv')
df_bubble$sort = 'bubble'

df_selection = read.csv('data_selection_sort.csv')
df_selection$sort = 'selection'

df_insertion = read.csv('data_insertion_sort.csv')
df_insertion$sort = 'insertion'

df_heap = read.csv('data_heapsort.csv')
df_heap$sort = 'heap'

df_merge = read.csv('data_mergesort.csv')
df_merge$sort = 'merge'

df_quick = read.csv('data_quicksort.csv')
df_quick$sort = 'quick'

df_combined = rbind(df_bogosort, df_bubble, df_selection, df_insertion, df_heap, df_merge, df_quick)

ggplot(df_combined, aes(x = num_items, y = time, color = as.factor(sort))) + 
  geom_line()

ggplot(df_combined[df_combined$num_items < 100 & df_combined$sort != 'bogo',], aes(x = num_items, y = time, color = as.factor(sort))) + 
  geom_line()

ggplot(df_combined[df_combined$num_items < 50 & df_combined$sort != 'bogo',], aes(x = num_items, y = time, color = as.factor(sort))) + 
  geom_line()


ggplot(df_combined[df_combined$sort %in% c('quick', 'heap', 'merge'),], aes(x = num_items, y = time, color = as.factor(sort))) + 
  geom_line()
