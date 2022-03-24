package com.school;

public class SentimentAnalysisUtils {

    public static String detectSentiment(String message) {

        Properties nlpProps = new Properties();
        nlpProps.setProperty("annotators", "tokenize, ssplit, pos, lemma, parse, sentiment");

        StanfordCoreNLP pipeline = new StanfordCoreNLP(nlpProps);

        Annotation annotation = pipeline.process(message);

        List<Double> sentiments = new ArrayList<>();
        List<Integer> sizes = new ArrayList<>();

        int longest = 0;
        int mainSentiment = 0;

        List<CoreMap> sentences = annotation.get(CoreAnnotations.SentencesAnnotation.class);
        for (CoreMap sentence : sentences) {
            Tree tree = sentence.get(SentimentCoreAnnotations.SentimentAnnotatedTree.class);
            int sentiment = RNNCoreAnnotations.getPredictedClass(tree);
            String partText = sentence.toString();

            if (partText.length() > longest) {
                mainSentiment = sentiment;
                longest = partText.length();
            }

            sentiments.add((double) sentiment);
            sizes.add(partText.length());

            //System.out.println("debug: " + sentiment);
            //System.out.println("size: " + partText.length());
        }



        return message;

        
    }


}
