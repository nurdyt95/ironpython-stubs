class GeneralTransformCollection(Animatable,ISealable,IAnimatable,IResource,IList,ICollection,IEnumerable,IList[GeneralTransform],ICollection[GeneralTransform],IEnumerable[GeneralTransform]):
 """
 Represents an ordered collection of System.Windows.Media.GeneralTransform objects.
 
 GeneralTransformCollection()
 GeneralTransformCollection(capacity: int)
 GeneralTransformCollection(collection: IEnumerable[GeneralTransform])
 """
 def Add(self,value):
  """
  Add(self: GeneralTransformCollection,value: GeneralTransform)
   Adds a System.Windows.Media.GeneralTransform object to the end of the 
    System.Windows.Media.GeneralTransformCollection.
  
  
   value: The System.Windows.Media.GeneralTransform to add to the end of the 
    System.Windows.Media.GeneralTransformCollection.
  """
  pass
 def Clear(self):
  """
  Clear(self: GeneralTransformCollection)
   Removes all System.Windows.Media.GeneralTransform objects from the 
    System.Windows.Media.GeneralTransformCollection.
  """
  pass
 def Clone(self):
  """
  Clone(self: GeneralTransformCollection) -> GeneralTransformCollection
  
   Creates a modifiable clone of this 
    System.Windows.Media.GeneralTransformCollection,making deep copies of this 
    object's values. When copying dependency properties,this method copies 
    resource references and data bindings (but they might no longer resolve) but 
    not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """ CloneCore(self: GeneralTransformCollection,source: Freezable) """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: GeneralTransformCollection) -> GeneralTransformCollection
  
   Creates a modifiable clone of this 
    System.Windows.Media.GeneralTransformCollection object,making deep copies of 
    this object's current values. Resource references,data bindings,and 
    animations are not copied,but their current values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """ CloneCurrentValueCore(self: GeneralTransformCollection,source: Freezable) """
  pass
 def Contains(self,value):
  """
  Contains(self: GeneralTransformCollection,value: GeneralTransform) -> bool
  
   Indicates whether the System.Windows.Media.GeneralTransformCollection contains 
    the specified System.Windows.Media.GeneralTransform object.
  
  
   value: The System.Windows.Media.GeneralTransform to locate in the 
    System.Windows.Media.GeneralTransformCollection.
  
   Returns: true if the collection contains value; otherwise false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: GeneralTransformCollection,array: Array[GeneralTransform],index: int)
   Copies the System.Windows.Media.GeneralTransform objects in the collection into 
    an array of GeneralTransforms,starting at the specified index position.
  
  
   array: The destination array.
   index: The zero-based index position where copying begins.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable
  
   Initializes a new instance of the System.Windows.Freezable class.
   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """ CreateInstanceCore(self: GeneralTransformCollection) -> Freezable """
  pass
 def FreezeCore(self,*args):
  """ FreezeCore(self: GeneralTransformCollection,isChecking: bool) -> bool """
  pass
 def GetAsFrozenCore(self,*args):
  """ GetAsFrozenCore(self: GeneralTransformCollection,source: Freezable) """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """ GetCurrentValueAsFrozenCore(self: GeneralTransformCollection,source: Freezable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: GeneralTransformCollection) -> Enumerator
  
   Returns an enumerator that can iterate through the collection.
   Returns: An enumerator that can iterate the collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: GeneralTransformCollection,value: GeneralTransform) -> int
  
   Searches for the specified System.Windows.Media.GeneralTransform object within 
    a System.Windows.Media.GeneralTransformCollection.
  
  
   value: The object to locate.
   Returns: The zero-based index position of value,if found; otherwise -1;
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: GeneralTransformCollection,index: int,value: GeneralTransform)
   Inserts a System.Windows.Media.GeneralTransform object into the specified index 
    position within the System.Windows.Media.GeneralTransformCollection.
  
  
   index: The zero-based index position to insert the object.
   value: The object to insert.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Freezable)
   Called when the current System.Windows.Freezable object is modified.
  """
  pass
 def OnFreezablePropertyChanged(self,*args):
  """
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject,property: DependencyProperty)
   This member supports the Windows Presentation Foundation (WPF) infrastructure 
    and is not intended to be used directly from your code.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
   property: The property that changed.
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject)
   Ensures that appropriate context pointers are established for a 
    System.Windows.DependencyObjectType data member that has just been set.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: Freezable,e: DependencyPropertyChangedEventArgs)
   Overrides the System.Windows.DependencyObject implementation of 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
    handlers in response to a changing dependency property of type 
    System.Windows.Freezable.
  
  
   e: Event data that contains information about which property changed,and its old 
    and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)
   Ensures that the System.Windows.Freezable is being accessed from a valid 
    thread. Inheritors of System.Windows.Freezable must call this method at the 
    beginning of any API that reads data members that are not dependency 
    properties.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: GeneralTransformCollection,value: GeneralTransform) -> bool
  
   Deletes a System.Windows.Media.GeneralTransform object from the 
    System.Windows.Media.GeneralTransformCollection.
  
  
   value: The object to remove.
   Returns: true if value was successfully deleted; otherwise false.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: GeneralTransformCollection,index: int)
   Deletes a System.Windows.Media.GeneralTransform object from the 
    System.Windows.Media.GeneralTransformCollection.
  
  
   index: The zero-based index position to remove the object.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)
   Raises the System.Windows.Freezable.Changed event for the 
    System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
    method. Classes that derive from System.Windows.Freezable should call this 
    method at the end of any API that modifies class members that are not stored as 
    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)
   Verifies that the System.Windows.Freezable is not frozen and that it is being 
    accessed from a valid threading context. System.Windows.Freezable inheritors 
    should call this method at the beginning of any API that writes to data members 
    that are not dependency properties.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: ICollection[GeneralTransform],item: GeneralTransform) -> bool
  __contains__(self: IList,value: object) -> bool
  
   Determines whether the System.Collections.IList contains a specific value.
  
   value: The object to locate in the System.Collections.IList.
   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,
    false.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,capacity: int)
  __new__(cls: type,collection: IEnumerable[GeneralTransform])
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of System.Windows.Media.GeneralTransform objects in the System.Windows.Media.GeneralTransformCollection.

Get: Count(self: GeneralTransformCollection) -> int

"""


 Enumerator=None

