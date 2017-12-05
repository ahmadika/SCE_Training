package org.deeplearning4j.examples.nlp.word2vec;

import org.deeplearning4j.models.embeddings.loader.WordVectorSerializer;
import org.deeplearning4j.models.word2vec.Word2Vec;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.util.Collection;

/**
 * Created by OmidDavtalab-SiminKarvigh.
 */
public class close_words_detector {

    private static Logger log = LoggerFactory.getLogger(close_words_detector.class);

    public static void main(String[] args) throws Exception {

        File locationToLoad = new File("vec.zip");
        log.info("Loading the saved model....");
        Word2Vec vec = WordVectorSerializer.readWord2VecModel(locationToLoad);
        // Prints out the closest 10 words to "xxxx". An example on what to do with these Word Vectors.
        log.info("Closest Words:");
        //Search terms should be first coverted to lower characters here and be inserted

        Collection<String> lst = vec.wordsNearest("iceberg", 5);
        System.out.println("5 Words closest to 'dust': " + lst);

        Collection<String> lst2 = vec.wordsNearest("water", 5);
        System.out.println("5 Words closest to 'water': " + lst2);

        Collection<String> lst3 = vec.wordsNearest("freezing", 5);
        System.out.println("5 Words closest to 'freezing': " + lst3);
    }
}
