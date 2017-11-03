
JFLAGS = -cp
JC = javac
WEKA = ./weka.jar

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $(WEKA) $*.java

CLASSES = \
	DataMiningProject1.java

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class


