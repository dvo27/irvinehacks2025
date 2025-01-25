import { View, Text, StyleSheet } from 'react-native';

export default function Tab() {
  return (
    <View style={styles.container}>
      <Text>Tabs: [Recipes|Scan|Inventory|Profile]</Text>
    </View>
  );
}

// recipes, scan, inventory, profile
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
