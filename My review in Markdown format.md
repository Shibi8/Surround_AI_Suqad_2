# Universal Language Model Fine-tuning for Text Classification #

##**SUMMARY:** 

Inductive exchange learning has incredibly affected PC vision, yet existing methodologies in NLP still require task-explicit changes and preparing starting with no outside help. We propose Universal Language Model Fine-tuning (ULMFiT), a compelling exchange learning strategy that can be connected to any undertaking in NLP, and present strategies that are key for fine-tuning a language model. Our strategy fundamentally beats the best in class on six content order undertakings, decreasing the blunder by 18-24% on most of datasets. Besides, with just 100 named models, it coordinates the execution of preparing without any preparation on 100x more information. We open source our pretrained models and code.They propose utilizing pre-trained models for comprehending a wide scope of NLP issues. With this methodology, you don't have to prepare your model without any preparation, however just fine-tune the first model. Their technique, called Universal Language Model Fine-Tuning (ULMFiT) beats best in class results, lessening the mistake by 18-24%. Significantly more, with just 100 marked precedents, ULMFiT matches the execution of models trained without any preparation on 10K named models. 


##**MAIN IDEA:**
*To address the absence of marked information and to make NLP characterization simpler and less tedious, the specialists propose applying exchange figuring out how to NLP issues. In this way, rather than preparing the model starting with no outside help, you can utilize another model that has been trained to tackle a comparative issue as the premise, and after that fine-tune the first model to take care of your particular issue.*

+	However, to be fruitful, this fine-tuning should consider a few essential contemplations: 
+	Different layers ought to be fine-tuned to various degrees as they catch various types of data. 
+	Fing all layers immediately is probably going to result in cataclysmic overlooking; hence, it is smarter to bit by bit unfreeze the model beginning from the last layer. 
 


## **FUTURE RESEARCH** ###

* Applying this new strategy to novel undertakings and models s (e.g., sequence labeling, natural language generation, entailment or question answering).

### APPLICATIONS: ###

Potentially, this method can also help with sequence-tagging and natural language generation.

+ ULMFiT can more efficiently solve a wide-range of NLP problems, including

+ Identifying spam, bots, offensive comments.
•Grouping articles by a specific feature.

+ Classifying positive and negative reviews;finding relevant documents etc.
